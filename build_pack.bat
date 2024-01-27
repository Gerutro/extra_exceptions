@echo off
title BUILD PACK
cd "C:\Users\gerut\PycharmProjects\extra_exceptions"
py -m build --sdist
py -m build --wheel
exit