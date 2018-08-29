# Split .str$ on .sep$ and store each found element in .array$ and
# length of .array$ in .length
#
# Usage:
#  include /path/to/this/script.praat
#  [code]
#  @split (SEPARATOR, STRING)
#  for i to split.length
#    str$[i] = split.array$[i]
#  endfor
#
# where SEPARATOR is a separator string and STRING is a string to
# separate.
#
# If string$ = "hello world", then after
# @split (" ", string$)
# split.array$[1] contains "hello" and split.array$[2] contains "world"
#
# Notes:
# - Since .length stores the number of items separated by a string, it is always
#   larger than the amount of occurences of that string by one, which means
#   it can be used to count occurences as well.
#
# - This script has been changed to use the new Praat syntax, which
#   started being introduced after v.5.3.44. It can be made to work with
#   the old syntax by replacing the definition to
#
#       procedure split .sep$ .str$
#
#   and, with the same example as above, calling it with
#
#       call split " " 'string$'
#
# Written by Jose J. Atria (28 February 2012)
# Last updated: 20 February 2014
#
# This script is free software: you can redistribute it and/or modify 
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# A copy of the GNU General Public License is available at
# <http://www.gnu.org/licenses/>.

procedure split (.sep$, .str$)
  .seplen = length(.sep$) 
  .length = 0
  repeat
    .strlen = length(.str$)
    .sep = index(.str$, .sep$)
    if .sep > 0
      .part$ = left$(.str$, .sep-1)
      .str$ = mid$(.str$, .sep+.seplen, .strlen)
    else
      .part$ = .str$
    endif
    .length = .length+1
    .array$[.length] = .part$
  until .sep = 0
endproc