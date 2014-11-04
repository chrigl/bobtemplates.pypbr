# -*- coding: utf-8 -*-
import re
from subprocess import check_output
from mrbob.bobexceptions import ValidationError

def get_git_global(field):
    return check_output(('git config --global %s' % field).split(' '))

def _author(configurator, question, field):
    """Try to get authors info via .mrbob or git"""
    author = None
    try:
        author = configurator.variables[field]
    except:
        pass
    if not author:
        try:
            author = get_git_global(field)
        except:
            pass
    if author:
        question.default = author.strip()

def pre_author(configurator, question):
    """Try to get authors name via user.name or git"""
    _author(configurator, question, 'user.name')

def pre_email(configurator, question):
    """Try to get authors email via user.email or git"""
    _author(configurator, question, 'user.email')

def pre_homepage(configurator, question):
    """Try to get authors homepage via user.homepage or git"""
    _author(configurator, question, 'user.homepage')

valid_pat_r = r'^[A-Za-z][A-Za-z\_]+$'
valid_pat = re.compile(valid_pat_r)

def validate_name(configurator, question, answer):
    """Validate packagename"""
    if not valid_pat.match(answer):
        raise ValidationError('Please use a name that matches %s' %
                valid_pat_r)
    return answer
