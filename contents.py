from pelican.contents import Content


class Resume(Content):
    default_status = 'published'
    default_template = 'resume/resume'


class About(Content):
    mandatory_properties = ('name', 'location')
    default_status = 'published'
    default_template = 'resume/about'


class Education(Content):
    mandatory_properties = ('title', 'institution', 'date', 'start', 'end')
    default_status = 'published'
    default_template = 'resume/education'


class Experience(Content):
    mandatory_properties = ('title', 'type', 'institution', 'date', 'start', 'end')
    default_status = 'published'
    default_template = 'resume/experience'


class Publication(Content):
    mandatory_properties = ('title', 'author', 'journal', 'year', 'publisher', 'doi', 'keywords')
    default_status = 'published'
    default_template = 'resume/publications'


class Certificate(Content):
    mandatory_properties = ('title', 'date', 'organization', 'doi')
    default_status = 'published'
    default_template = 'resume/publications'


class Extra(Content):
    mandatory_properties = ('title',)
    default_status = 'published'
    default_template = 'resume/extras'


class Skills(Content):
    mandatory_properties = ('title',)
    default_status = 'published'
    default_template = 'resume/skills'
