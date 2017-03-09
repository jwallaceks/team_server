#!/bin/sh

nohup curl http://joel.oeie.org:5138/blink1/on --max-time 5 --connect-timeout 60 &
nohup curl http://trent.oeie.org:5138/blink1/on --max-time 5 --connect-timeout 60 &
nohup curl http://jessie.oeie.org:5138/blink1/on --max-time 5 --connect-timeout 60 &
nohup curl http://zac.oeie.org:5138/blink1/on --max-time 5 --connect-timeout 60 &