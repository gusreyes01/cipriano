#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext


def landing(request):
	return render_to_response('website/coming-soon.html', {}, context_instance=RequestContext(request))
