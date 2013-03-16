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

from fretboard import Fretboard, MAX_STRING, MAX_FRET
from random import randrange

guitar = Fretboard(['E', 'A', 'D', 'G', 'B', 'E'])

questions = input("Number of questions? ")
if questions < 1:
    raise ValueError("Invalid value")

max_fret = input("Maximum fret number? ")
if max_fret < 1 or max_fret > MAX_FRET:
    raise ValueError("Invalid value")

correct_questions = 0

for i in range(questions):
    string = randrange(1, MAX_STRING + 1)
    fret = randrange(1, max_fret + 1)
    note = guitar.get_note_at_string_and_fret(string, fret)

    answer = raw_input("Note at fret " + str(fret) + " in string " + str(string) + "? ")
    if answer == note:
        print "Correct!"
        correct_questions += 1
    else:
        print "FAIL! The answer was " + note

print "You answered correctly " + str(correct_questions) + " of " + str(questions) + " questions"
print "Your success rate is " + str(round(float(correct_questions) / float(questions) * 100, 2)) + "%"
