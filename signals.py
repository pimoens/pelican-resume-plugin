from blinker import signal


resume_generator_init = signal('resume_generator_init')
resume_generator_finalized = signal('resume_generator_finalized')
