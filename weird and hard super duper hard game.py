#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 16:22:07 2025

@author: ido
"""

score=0
print('guess the animal')
answer=input('which bear lives at the northpole? ')
if answer=='polar bear':
  print('correct!')
  score = score + 1
xelse:
  answer=input('sorry wrong answer try again. ')
  if answer=='polar bear':
    print('correct!')
    score + score + 1
  else:
    answer=input('sorry wrong answer try again. ')
    if answer=='polar bear':
        print('correct')
        score = score + 1
    else:
        print('the correct answer is polar bear')
print('your score is', score)
answer=input('which is the fastest land animal? ')
if answer=='cheetah':
  print('correct!')
  score = score + 1
else:
  answer=input('sorry wrong answer try again. ')
  if answer=='cheetah':
    print('correct!')
    score + score + 1
  else:
    answer=input('sorry wrong answer try again. ')
    if answer=='cheetah':
        print('correct')
        score = score + 1
    else:
        print('the correct answer is cheetah')
print('your score is', score)
answer=input('which is the largest animal? ')
if answer=='blue whale':
  print('correct!')
  score = score + 1
else:
  answer=input('sorry wrong answer try again. ')
  if answer=='blue whale':
    print('correct!')
    score + score + 1
  else:
    answer=input('sorry wrong answer try again. ')
    if answer=='blue whale':
        print('correct')
        score = score + 1
    else:
        print('sorry the correct answer is blue whale')
print('your score is', score)