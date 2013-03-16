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
MAX_FRET = 22
MAX_STRING = 6

class String(object):
    def __init__(self, key):
        self.key = key
        self.key_offset = NOTES.index(key)

    def get_key(self):
        return self.key

    def get_note_at_fret(self, fret):
        if fret < 0 or fret > MAX_FRET:
            raise ValueError("Invalid fret number")

        pos = (self.key_offset + fret) % len(NOTES)
        return NOTES[pos]

class Fretboard(object):
    def __init__(self, tuning):
        tuning.reverse()
        self.strings = []
        for key in tuning:
            self.strings.append(String(key))

    def get_note_at_string_and_fret(self, string, fret):
        if string < 1 or string > MAX_STRING:
            raise ValueError("Invalid string number")
        return self.strings[string - 1].get_note_at_fret(fret)

    def get_strings(self):
        return self.strings

    def print_notes(self, min_fret, max_fret, notes=NOTES):
        self._print_border(min_fret, max_fret)
        num = 1
        for string in self.strings:
            self._print_string(num, string, min_fret, max_fret, notes)
            self._print_border(min_fret, max_fret)
            num += 1
        self._print_inlays(min_fret, max_fret)

    def _print_string(self, num, string, min_fret, max_fret, notes):
        line = str(num) + ' '
        for fret in range(min_fret, max_fret + 1):
            note = string.get_note_at_fret(fret)
            if not note in notes:
                note = ' '
            if len(note) == 1:
                note += ' '
            line += '| ' + note + ' '
        print line + '|'

    def _print_border(self, min_fret, max_fret):
        print (' ' * 2) + ('-' * ((max_fret - min_fret + 1) * 5 + 1))

    def _print_inlays(self, min_fret, max_fret):
        line = ' ' * 3
        for i in range(min_fret, max_fret + 1):
            line += ' '
            if (i == 12) or ((i % 2 != 0) and (i != 1) and (i != 11) and (i != 13)):
                line += str(i)
                if i < 10:
                    line += ' ' * 2
                else:
                    line += ' '
            else:
                line += ' ' * 3
            line += ' '
        print line

def main():
    guitar = Fretboard(['E', 'A', 'D', 'G', 'B', 'E'])
    guitar.print_notes(1, 22, ['A', 'B', 'C', 'F', 'G'])

if __name__ == '__main__':
    main()
