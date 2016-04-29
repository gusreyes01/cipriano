#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render


def landing(request):
	return render(request, 'website/coming-soon.html', {})


def home(request):
	return render(request, 'website/home.html', {})


def contact(request):
	return render(request, 'website/contact.html', {})


def studio(request):
	return render(request, 'website/studio.html', {})
