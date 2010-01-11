===============
django-feedback
===============

Django Feedback is a simple Django application that makes it trivialto start accepting user feedback 
from authenticated users within your Django project.

Installation
============

Put ``feedback`` in your ``INSTALLED_APPS``, and set ``FEEDBACK_CHOICES`` to a 2-tuple of feedback types
in your settings file. For example:

.. code-block:: python

FEEDBACK_CHOICES = (
	('bug', 'Bug'),
	('feature_request', 'Feature Request)
)

Add ``feedback.context_processors.feedback_form`` to ``TEMPLATE_CONTEXT_PROCESSORS``, and
``feedback_form`` will be in the context for all authenticated users.

Screenshots
===========
.. image:: http://cloud.github.com/downloads/girasquid/django-feedback/django-feedback-1.PNG

Overview in your admin index. Allows you to see all feedback current in the system.

.. image:: http://cloud.github.com/downloads/girasquid/django-feedback/django-feedback-2.PNG

Viewing a piece of feedback from a user.