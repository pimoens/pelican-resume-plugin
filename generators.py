import logging
import os
from pelican.generators import CachingGenerator

from .contents import About, Education, Experience, Publication, Certificate, Extra, Resume, Skill

logger = logging.getLogger(__name__)


class ResumeGenerator(CachingGenerator):

    def __init__(self, *args, **kwargs):
        self.about = None
        self.education = []
        self.experience = {}
        self.publications = []
        self.certificates = []
        self.skills = {}
        self.extras = []

        self.parts = [
            ('extras', Extra, self.extras)
        ]

        super().__init__(*args, **kwargs)
        # resume_generator_init.send(self)

    def generate_about_section(self):
        f = os.path.join(self.settings['RESUME_PATH'], 'about.md')
        data = self.get_cached_data(f, None)
        if data is None:
            try:
                data = self.readers.read_file(
                    base_path=self.path, path=f, content_class=Experience,
                    context=self.context
                )
            except Exception as e:
                logger.error(
                    'Could not process %s\n%s', f, e,
                    exc_info=self.settings.get('DEBUG', False))
                self._add_failed_source_path(f)

            if not data.is_valid():
                self._add_failed_source_path(f)

            self.cache_data(f, data)

        self.about = data

        self._update_context(('about',))

    def generate_experience_section(self):
        base_path = os.path.join(self.settings['RESUME_PATH'], 'experience')
        for f in self.get_files(
            base_path
        ):
            data = self.get_cached_data(f, None)
            if data is None:
                try:
                    data = self.readers.read_file(
                        base_path=self.path, path=f, content_class=Experience,
                        context=self.context
                    )
                except Exception as e:
                    logger.error(
                        'Could not process %s\n%s', f, e,
                        exc_info=self.settings.get('DEBUG', False))
                    self._add_failed_source_path(f)

                if not data.is_valid():
                    self._add_failed_source_path(f)

                self.cache_data(f, data)

            tree = f.replace(base_path, '').split('/')[1:-1]
            tree = [name.replace('-', ' ').replace('_', ' ') for name in tree]

            def add_data_recursive(dict_, tree_, data_):
                node = tree_[0]

                if node not in dict_.keys():
                    dict_[node] = {'_items': []}

                if len(tree_) == 1:
                    dict_[node]['_items'].append(data_)
                    dict_[node]['_items'] = list(
                        sorted(dict_[node]['_items'], key=lambda experience: experience.date,
                               reverse=True))
                else:
                    add_data_recursive(dict_[node], tree_[1:], data_)

            add_data_recursive(self.experience, tree, data)

        self._update_context(('experience',))

    def generate_education_section(self):
        for f in self.get_files(
            os.path.join(self.settings['RESUME_PATH'], 'education')
        ):
            data = self.get_cached_data(f, None)
            if data is None:
                try:
                    data = self.readers.read_file(
                        base_path=self.path, path=f, content_class=Education,
                        context=self.context
                    )
                except Exception as e:
                    logger.error(
                        'Could not process %s\n%s', f, e,
                        exc_info=self.settings.get('DEBUG', False))
                    self._add_failed_source_path(f)

                if not data.is_valid():
                    self._add_failed_source_path(f)

                self.cache_data(f, data)

            self.education.append(data)
        self.education = list(sorted(self.education, key=lambda education: education.date, reverse=True))

        self._update_context(('education',))

    def generate_publications_section(self):
        for f in self.get_files(
            os.path.join(self.settings['RESUME_PATH'], 'publications')
        ):
            data = self.get_cached_data(f, None)
            if data is None:
                try:
                    data = self.readers.read_file(
                        base_path=self.path, path=f, content_class=Publication,
                        context=self.context
                    )
                except Exception as e:
                    logger.error(
                        'Could not process %s\n%s', f, e,
                        exc_info=self.settings.get('DEBUG', False))
                    self._add_failed_source_path(f)

                if not data.is_valid():
                    self._add_failed_source_path(f)

                self.cache_data(f, data)

            self.publications.append(data)
        self.publications = list(sorted(self.publications, key=lambda publication: publication.year, reverse=True))

        self._update_context(('publications',))

    def generate_certificates_section(self):
        for f in self.get_files(
            os.path.join(self.settings['RESUME_PATH'], 'certificates')
        ):
            data = self.get_cached_data(f, None)
            if data is None:
                try:
                    data = self.readers.read_file(
                        base_path=self.path, path=f, content_class=Certificate,
                        context=self.context
                    )
                except Exception as e:
                    logger.error(
                        'Could not process %s\n%s', f, e,
                        exc_info=self.settings.get('DEBUG', False))
                    self._add_failed_source_path(f)

                if not data.is_valid():
                    self._add_failed_source_path(f)

                self.cache_data(f, data)

            self.certificates.append(data)
        self.certificates = list(sorted(self.certificates, key=lambda certificate: certificate.date, reverse=True))

        self._update_context(('certificates',))

    def generate_skills_section(self):
        base_path = os.path.join(self.settings['RESUME_PATH'], 'skills')
        for f in self.get_files(
            base_path
        ):
            data = self.get_cached_data(f, None)
            if data is None:
                try:
                    data = self.readers.read_file(
                        base_path=self.path, path=f, content_class=Skill,
                        context=self.context
                    )
                except Exception as e:
                    logger.error(
                        'Could not process %s\n%s', f, e,
                        exc_info=self.settings.get('DEBUG', False))
                    self._add_failed_source_path(f)

                if not data.is_valid():
                    self._add_failed_source_path(f)

                self.cache_data(f, data)

            tree = f.replace(base_path, '').split('/')[1:-1]
            tree = [name.replace('-', ' ').replace('_', ' ') for name in tree]

            def add_data_recursive(dict_, tree_, data_):
                node = tree_[0]

                if node not in dict_.keys():
                    dict_[node] = {'_items': []}

                if len(tree_) == 1:
                    dict_[node]['_items'].append(data_)
                    dict_[node]['_items'] = list(sorted(dict_[node]['_items'], key=lambda skill: int(skill.level), reverse=True))
                else:
                    add_data_recursive(dict_[node], tree_[1:], data_)

            add_data_recursive(self.skills, tree, data)

        self._update_context(('skills',))

    def generate_context(self):
        self.generate_about_section()
        self.generate_experience_section()
        self.generate_education_section()
        self.generate_publications_section()
        self.generate_certificates_section()
        self.generate_skills_section()

        for name, cls, list_ in self.parts:
            for f in self.get_files(
                    os.path.join(self.settings['RESUME_PATH'], name)
            ):
                data = self.get_cached_data(f, None)
                if data is None:
                    try:
                        data = self.readers.read_file(
                            base_path=self.path, path=f, content_class=cls,
                            context=self.context
                        )
                    except Exception as e:
                        logger.error(
                            'Could not process %s\n%s', f, e,
                            exc_info=self.settings.get('DEBUG', False))
                        self._add_failed_source_path(f)

                    if not data.is_valid():
                        self._add_failed_source_path(f)

                    self.cache_data(f, data)

                list_.append(data)

            self._update_context((name,))

        self.save_cache()
        self.readers.save_cache()

        # resume_generator_finalized.send(self)

    def generate_output(self, writer):
        metadata = {
            'about': self.about,
            'experience': self.experience,
            'education': self.education,
            'publications': self.publications,
            'certificates': self.certificates,
            'skills': self.skills
        }
        for name, cls, list_ in self.parts:
            metadata[name] = list_
        writer.write_file(
            self.settings['RESUME_SAVE_AS'], self.get_template(Resume.default_template),
            self.context, resume=metadata,
            relative_urls=self.settings['RELATIVE_URLS'],
            url=self.settings['RESUME_URL'])
