#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2013 José Antonio Calvo Fernández <jacalvo@zentyal.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

NOTES = ('A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#')
MAX_FRET_NUMBER = 22

class String(object):
    def __init__(self, key):
        self.key = key
        self.key_offset = NOTES.index(key)

    def get_key(self):
        return self.key

    def get_note_at_fret(self, fret):
        if fret < 0 or fret > MAX_FRET_NUMBER:
            raise Error("Invalid fret number")

        pos = (self.key_offset + fret) % len(NOTES)
        return NOTES[pos]

class Fretboard(object):
    def __init__(self, tuning):
        tuning.reverse()
        self.strings = []
        for key in tuning:
            self.strings.append(String(key))

    def get_strings(self):
        return self.strings

    def print_notes(self, max_fret):
        for string in self.strings:
            for fret in range(max_fret):
                print string.get_note_at_fret(fret),
            print

def main():
    guitar = Fretboard(['E', 'A', 'D', 'G', 'B', 'E'])
    guitar.print_notes(12)

if __name__ == '__main__':
    main()
