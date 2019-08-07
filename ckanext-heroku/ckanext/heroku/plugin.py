from os import environ

from ckan import plugins
from ckan.plugins import toolkit

CONFIG_FROM_HEROKU_CONFIG = {
    'ckan.redis.url': 'REDISTOGO_URL',
    'solr_url': 'WEBSOLR_URL',
}


class HerokuPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config):
        for option, env in CONFIG_FROM_HEROKU_CONFIG.items():
            from_env = environ.get(env)

            if from_env:
                config[option] = from_env
