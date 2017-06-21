# -*- coding: utf-8 -*-
"""
tkFileBrowser - Alternative to filedialog for Tkinter
Copyright 2017 Juliette Monsel <j_4321@protonmail.com>

tkFileBrowser is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

tkFileBrowser is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


The icons are modified versions of icons from the elementary project
(the xfce fork to be precise https://github.com/shimmerproject/elementary-xfce)
Copyright 2007-2013 elementary LLC.


Recent files management
"""


class RecentFiles:
    """ Recent files manager """
    def __init__(self, filename, nbmax=30):
        self._filename = filename
        self.nbmax = nbmax
        self._files = [] # most recent files first
        try:
            with open(filename) as file:
                self._files = file.read().split()
        except Exception:
            pass

    def get(self):
        return self._files

    def add(self, file):
        print(file, self._files, file in self._files)
        if not file in self._files:
            self._files.insert(0, file)
            if len(self._files) > self.nbmax:
                del(self._files[-1])
        else:
            self._files.remove(file)
            self._files.insert(0, file)
        with open(self._filename, 'w') as file:
            file.write('\n'.join(self._files))
