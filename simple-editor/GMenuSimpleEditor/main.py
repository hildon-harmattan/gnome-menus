#
# Copyright (C) 2005 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#

def main (args):
    import locale
    import gettext

    import pygtk; pygtk.require('2.0');

    import gtk
    import gtk.glade

    import maindialog
    import config

    locale.setlocale (locale.LC_ALL, "")
    gettext.install (config.PACKAGE, config.LOCALEDIR)
    gtk.glade.bindtextdomain (config.PACKAGE, config.LOCALEDIR)

    dialog = maindialog.MenuEditorDialog (args)

    gtk.main ()
