"""Zigate base view."""
from homeassistant.components.http import HomeAssistantView
from ...const import VIEWS


class ZigateViewBase(HomeAssistantView):
    """Base View Class for Zigate."""

    requires_auth = False
    data = {"task_running": False}

    @property
    def base_content(self):
        """Base content."""
        return """
            <head>
                {}
            </head>
            <body>
            {}
            <div id="main" class="zigate-content">
            {}
        """.format(
            self.imports, self.header, self.progress_bar
        )

    @property
    def imports(self):
        """Load imports."""
        return """
        <link rel="stylesheet" href="{static}/zigate.css">
        <script src="{static}/zigate.js"></script>
        """.format(
            static=VIEWS["network"]["slug"]
        )

    @property
    def header(self):
        """Load header."""
        return """
        <div class="navbar-fixed">
          <nav class="nav-extended zigate-nav">
            <div class="nav-content">
              <ul class="right tabs tabs-transparent">
                <li class="tab"><a href="{}">overview</a></li>
                <li class="tab"><a href="{}">store</a></li>
                <li class="tab right"><a href="{}">settings</a></li>
              </ul>
            </div>
          </nav>
        </div>
        """.format(
            VIEWS["network"]["slug"],
            VIEWS["network"]["slug"],
            VIEWS["network"]["slug"]
        )

    @property
    def progress_bar(self):
        """Load progress bar."""
        if self.data["task_running"]:
            display = "block"
        else:
            display = "none"

        return """
        <div style="display: {}">
        <p>Background task running, refresh the page in a little while.</p>
        </div>
        <div class="progress zigate-bar-background"
             id="progressbar" style="display: {}">
            <div class="indeterminate zigate-bar"></div>
        </div>
        """.format(
            display, display
        )

    @property
    def footer(self):
        """Return the end of the document."""
        return "</div></body>"
