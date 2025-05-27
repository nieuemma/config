# Call autoconfig
config.load_autoconfig()

# set qutebrowser colors
dblue = "#0a0c10"
red = "#ff9492"
green = "#26cd4d"
yellow  = "#f0b72f"
blue = "#71b7ff"
purple = "#cb9eff"
turq = "#39c5cf"
white = "#d9dee3"
dblueb = "#0d1117"
redb = "#ffb1af"
greenb = "#4ae168"
yellowb = "#f7c843"
blueb = "#91cbff"
purpleb = "#dbb7ff"
turqb = "#56d4dd"
whiteb = "#ffffff"

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = white

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = dblueb

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = dblue

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = green

# Background color of the completion widget category headers.
c.colors.completion.category.bg = dblue

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = dblue

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = dblue

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = green

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = blue

# Top border color of the selected completion item.
c.colors.completion.item.selected.border.top = blue

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = blue

# Foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = greenb

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = greenb

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = dblueb

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = dblue

# Background color of disabled items in the context menu.
c.colors.contextmenu.disabled.bg = dblue

# Foreground color of disabled items in the context menu.
c.colors.contextmenu.disabled.fg = dblueb

# Background color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.bg = dblue

# Foreground color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.fg =  white

# Background color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.bg = blue

#Foreground color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.fg = green

# Background color for the download bar.
c.colors.downloads.bar.bg = dblue

# Color gradient start for download text.
c.colors.downloads.start.fg = white

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = green

# Color gradient end for download text.
c.colors.downloads.stop.fg = whiteb

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = greenb

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = red

# Font color for hints.
c.colors.hints.fg = white

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = dblue

# Font color for the matched part of hints.
c.colors.hints.match.fg = green

# Text color for the keyhint widget.
c.colors.keyhint.fg = white

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = dblueb

# Background color of the keyhint widget.
c.colors.keyhint.bg = dblue

# Foreground color of an error message.
c.colors.messages.error.fg = whiteb

# Background color of an error message.
c.colors.messages.error.bg = red

# Border color of an error message.
c.colors.messages.error.border = red

# Foreground color of a warning message.
c.colors.messages.warning.fg = white

# Background color of a warning message.
c.colors.messages.warning.bg = redb

# Border color of a warning message.
c.colors.messages.warning.border = redb

# Foreground color of an info message.
c.colors.messages.info.fg = white

# Background color of an info message.
c.colors.messages.info.bg = dblue

# Border color of an info message.
c.colors.messages.info.border = dblue

# Foreground color for prompts.
c.colors.prompts.fg = white

# Border used around UI elements in prompts.
c.colors.prompts.border = dblue

# Background color for prompts.
c.colors.prompts.bg = dblue

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = dblueb

# Foreground color for the selected item in filename prompts.
c.colors.prompts.selected.fg = white

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = greenb

# Background color of the statusbar.
c.colors.statusbar.normal.bg = dblue

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = white

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = green

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = white

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = greenb

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = white

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = dblue

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = white

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = dblue

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = white

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = dblue

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = dblue

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = redb

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = dblue

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = green

# Background color of the progress bar.
c.colors.statusbar.progress.bg = green

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = dblueb

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = red

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = dblueb

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = greenb

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = greenb

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = redb

# Background color of the tab bar.
c.colors.tabs.bar.bg = dblue

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = green

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = greenb

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = red

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = dblue

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = dblue

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = dblue

# Background color of unselected even tabs.
c.colors.tabs.even.bg = dblue

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = dblue

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = dblue

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = dblue

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = dblue

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = dblue

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = whiteb

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = dblue

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = whiteb

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = whiteb

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = dblue

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = whiteb

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = dblue

# Background color for webpages if unset (or empty to use the theme's color).
c.colors.webpage.bg = dblue
