#!/usr/bin/env python
# -*- coding: utf-8 -*-

# views.py créer les vue pour les renvoier au navigateur à partir des fonctions définit ici

from django.shortcuts import render
from django.http import HttpResponseRedirect

from datetime import date

def hls_index(request) :

		return render(request, 'hls_index.html', {})
