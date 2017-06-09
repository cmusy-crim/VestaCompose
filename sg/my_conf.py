"""
Updated values for ServiceGateway in Vesta context.
"""

SECURITY = {"BYPASS_SECURITY": True}

CELERY = {
    'BROKER_URL': "amqp://amqp",
    "CELERY_RESULT_BACKEND": "amqp",
    'CELERY_TASK_SERIALIZER': "json",
    'CELERY_RESULT_SERIALIZER': "json",
    'CELERY_ACCEPT_CONTENT': ["json"]}

DATABASES = {
    'Invocations': {
        'filename': "/mnt/volume/service_invocations.db",
        'schema_filename':
            "/usr/lib/python2.7/site-packages/"
            "ServiceGateway/static/"
            "service_invocations_schema.sql"
        },
    'Requests': {
        'filename': "/mnt/volume/requests.db",
        'schema_filename':
            "/usr/lib/python2.7/site-packages/"
            "ServiceGateway/static/"
            "requests_schema.sql"
        }
    }

CELERY_PROJ_NAME = "worker"

GET_STORAGE_DOC_REQ_URL = "http://mss:5000/get/{storage_doc_id}"

WORKER_SERVICES = {
    'stub': {
        # Keyword used in the rest api to access this service
        # (ex.: http://server/<route_keyword>/info)
        # Set to '.' to access this service without keyword
        # (ex.: http://server/info)
        'route_keyword': 'stub',

        # The celery task name.
        # Must match the task in the worker app name : <proj_name>.<task_name>
        # (ex.: diarisation)
        'celery_task_name': 'stub',

        # The celery queue name.
        # Must match the queue name specified when starting the worker
        # (by the -Q switch)
        'celery_queue_name': 'stub',

        # Following parameters are required by the CANARIE API (info request)
        'name': 'Stub service',
        'synopsis': "RESTful service providing service stub.",
        'version': "0.2.0",  # Expected version - will check!
        'institution': 'CRIM',
        'releaseTime': '2015-01-01T00:00:00Z',
        'supportEmail': 'info-cra@crim.ca',
        'category': "Data Manipulation",
        'researchSubject': "system integration",
        'tags': "stub",

        # The following parameters are used to respond to some CANARIE API
        # request.
        #
        # They must be one of the following:
        #  - A valid URL to perform a redirection
        #  - A relative template file that will be used to generate the HTML
        #    page (relative to the templates directory)
        #  - A response string and the html status separated by a comma that
        #    will be used  to make a response to the requested element. Ex.:
        #    'Not available,404'

        'home': "https://github.com/crim-ca/Service",
        'doc': "https://github.com/crim-ca/Service",
        'releasenotes': "https://github.com/crim-ca/Service",
        'support': "https://github.com/crim-ca/Service",


        # If the source are not provided, CANARIE requires a 204 (No content)
        # response
        'source': "https://github.com/crim-ca/Service",
        'tryme': "https://github.com/crim-ca/Service",
        'licence': "https://github.com/crim-ca/Service",
        'provenance': "https://github.com/crim-ca/Service",
        'os_args': {'image':
                    'docker-registry.crim.ca/vesta/service-stub:latest',
                    'instance_type': 'm1.tiny'},
        'rubber_params': {'spawn_ratio': 0.01}
    },
    'musictrans': {
        # Keyword used in the rest api to access this service
        # (ex.: http://server/<route_keyword>/info)
        # Set to '.' to access this service without keyword
        # (ex.: http://server/info)
        'route_keyword': 'musictrans',

        # The celery task name.
        'celery_task_name': 'music_transcription',

        # The celery queue name.
        # Must match the queue name specified when starting the worker
        # (by the -Q switch)
        'celery_queue_name': 'musictrans',

        # Following parameters are required by the CANARIE API (info request)
        'name': 'Stub service',
        'synopsis': "RESTful service providing service musictrans.",
        'version': "0.8.0",  # Expected version - will check!
        'institution': 'CRIM',
        'releaseTime': '2015-01-01T00:00:00Z',
        'supportEmail': 'info-cra@crim.ca',
        'category': "Data Manipulation",
        'researchSubject': "system integration",
        'tags': "musictrans",

        # The following parameters are used to respond to some CANARIE API
        # request.
        #
        # They must be one of the following:
        #  - A valid URL to perform a redirection
        #  - A relative template file that will be used to generate the HTML
        #    page (relative to the templates directory)
        #  - A response string and the html status separated by a comma that
        #    will be used  to make a response to the requested element. Ex.:
        #    'Not available,404'

        'home': "https://github.com/crim-ca/Service",
        'doc': "https://github.com/crim-ca/Service",
        'releasenotes': "https://github.com/crim-ca/Service",
        'support': "https://github.com/crim-ca/Service",


        # If the source are not provided, CANARIE requires a 204 (No content)
        # response
        'source': "https://github.com/crim-ca/Service",
        'tryme': "https://github.com/crim-ca/Service",
        'licence': "https://github.com/crim-ca/Service",
        'provenance': "https://github.com/crim-ca/Service",
        'os_args': {'image':
                    'docker-registry.crim.ca/vesta/service-dia:latest',
                    'instance_type': 'm1.tiny'},
        'rubber_params': {'spawn_ratio': 0.01}
    },
    'diarisation': {
        # Keyword used in the rest api to access this service
        # (ex.: http://server/<route_keyword>/info)
        # Set to '.' to access this service without keyword
        # (ex.: http://server/info)
        'route_keyword': 'diarisation',

        # The celery task name.
        # Must match the task in the worker app name : <proj_name>.<task_name>
        # (ex.: diarisation)
        'celery_task_name': 'diarisation',

        # The celery queue name.
        # Must match the queue name specified when starting the worker
        # (by the -Q switch)
        'celery_queue_name': 'diarisation',

        # Following parameters are required by the CANARIE API (info request)
        'name': 'Stub service',
        'synopsis': "RESTful service providing service diarisation.",
        'version': "0.7.3",  # Expected version - will check!
        'institution': 'CRIM',
        'releaseTime': '2015-01-01T00:00:00Z',
        'supportEmail': 'info-cra@crim.ca',
        'category': "Data Manipulation",
        'researchSubject': "system integration",
        'tags': "diarisation",

        # The following parameters are used to respond to some CANARIE API
        # request.
        #
        # They must be one of the following:
        #  - A valid URL to perform a redirection
        #  - A relative template file that will be used to generate the HTML
        #    page (relative to the templates directory)
        #  - A response string and the html status separated by a comma that
        #    will be used  to make a response to the requested element. Ex.:
        #    'Not available,404'

        'home': "https://github.com/crim-ca/Service",
        'doc': "https://github.com/crim-ca/Service",
        'releasenotes': "https://github.com/crim-ca/Service",
        'support': "https://github.com/crim-ca/Service",


        # If the source are not provided, CANARIE requires a 204 (No content)
        # response
        'source': "https://github.com/crim-ca/Service",
        'tryme': "https://github.com/crim-ca/Service",
        'licence': "https://github.com/crim-ca/Service",
        'provenance': "https://github.com/crim-ca/Service",
        'os_args': {'image':
                    'docker-registry.crim.ca/vesta/service-dia:latest',
                    'instance_type': 'm1.tiny'},
        'rubber_params': {'spawn_ratio': 0.01}
    },
    'STT': {
        # Keyword used in the rest api to access this service
        # (ex.: http://server/<route_keyword>/info)
        # Set to '.' to access this service without keyword
        # (ex.: http://server/info)
        'route_keyword': 'STT',

        # The celery task name.
        # Must match the task in the worker app name : <proj_name>.<task_name>
        # (ex.: STT)
        'celery_task_name': 'STT',

        # The celery queue name.
        # Must match the queue name specified when starting the worker
        # (by the -Q switch)
        'celery_queue_name': 'stt',

        # Following parameters are required by the CANARIE API (info request)
        'name': 'Stub service',
        'synopsis': "RESTful service providing service STT.",
        'version': "0.7.3",  # Expected version - will check!
        'institution': 'CRIM',
        'releaseTime': '2015-01-01T00:00:00Z',
        'supportEmail': 'info-cra@crim.ca',
        'category': "Data Manipulation",
        'researchSubject': "system integration",
        'tags': "STT",

        # The following parameters are used to respond to some CANARIE API
        # request.
        #
        # They must be one of the following:
        #  - A valid URL to perform a redirection
        #  - A relative template file that will be used to generate the HTML
        #    page (relative to the templates directory)
        #  - A response string and the html status separated by a comma that
        #    will be used  to make a response to the requested element. Ex.:
        #    'Not available,404'

        'home': "https://github.com/crim-ca/Service",
        'doc': "https://github.com/crim-ca/Service",
        'releasenotes': "https://github.com/crim-ca/Service",
        'support': "https://github.com/crim-ca/Service",


        # If the source are not provided, CANARIE requires a 204 (No content)
        # response
        'source': "https://github.com/crim-ca/Service",
        'tryme': "https://github.com/crim-ca/Service",
        'licence': "https://github.com/crim-ca/Service",
        'provenance': "https://github.com/crim-ca/Service",
        'os_args': {'image':
                    'docker-registry.crim.ca/vesta/service-dia:latest',
                    'instance_type': 'm1.tiny'},
        'rubber_params': {'spawn_ratio': 0.01}
    },
    'SPV': {
        'route_keyword': 'SPV',
        'celery_task_name': 'STT_SPV',
        'celery_queue_name': 'STT',
        'name': 'Service SPV',
        'synopsis': ("RESTful service providing vocabulary personnalisation "
                     "interface."),
        'version': '0.8.2',  # Expected version - will check.
        'institution': 'CRIM',
        'releaseTime': '2015-01-01T00:00:00Z',
        'supportEmail': 'support-vesta@crim.ca',
        'category': "Data Manipulation",
        'researchSubject': "Speech analysis",
        'tags': "STT,speech,recognition,transcription,vocabulary",
        'home': "https://github.com/crim-ca/Service",
        'doc': "https://github.com/crim-ca/Service",
        'releasenotes': "https://github.com/crim-ca/Service",
        'support': "https://github.com/crim-ca/Service",


        # If the source are not provided, CANARIE requires a 204 (No content)
        # response
        'source': "https://github.com/crim-ca/Service",
        'tryme': "https://github.com/crim-ca/Service",
        'licence': "https://github.com/crim-ca/Service",
        'provenance': "https://github.com/crim-ca/Service",
        'os_args': {'image': 'my_service_image_name_v_0.1.0',
                    'instance_type': 'm1.large'},
        # Process-request to spawn VM ratio
        'rubber_params': {'spawn_ratio': 0.1}
    },
    'matching': {
        'route_keyword': 'matching',
        'celery_task_name': 'matching',
        'celery_queue_name': 'matching',
        'name': 'Matching Service',
        'synopsis': "RESTful service providing text to audio matching.",
        'version': '0.1.2',  # Expected version
        'institution': 'CRIM',
        'releaseTime': '2015-01-01T00:00:00Z',
        'supportEmail': 'vesta-support@crim.ca',
        'category': "Data Manipulation",
        'researchSubject': "Speech analysis",
        'tags': "text,speech,matching,audio,audio mining",
        'home': "https://github.com/crim-ca/Service",
        'doc': "https://github.com/crim-ca/Service",
        'releasenotes': "https://github.com/crim-ca/Service",
        'support': "https://github.com/crim-ca/Service",


        # If the source are not provided, CANARIE requires a 204 (No content)
        # response
        'source': "https://github.com/crim-ca/Service",
        'tryme': "https://github.com/crim-ca/Service",
        'licence': "https://github.com/crim-ca/Service",
        'provenance': "https://github.com/crim-ca/Service",
        'os_args': {'image': 'my_service_image_name_v_0.1.0',
                    'instance_type': 'm1.large'},
        # Process-request to spawn VM ratio
        'rubber_params': {'spawn_ratio': 0.1}
    },
    'transition': {
        'route_keyword': 'transition',
        'celery_task_name': 'transition',
        'celery_queue_name': 'transition',
        'name': 'Transition detection service',
        'synopsis': "RESTful service providing transition detection in video.",
        'version': '1.1.5',  # Expected version - will check.
        'institution': 'CRIM',
        'releaseTime': '2015-01-01T00:00:00Z',
        'supportEmail': 'support-vesta@crim.ca',
        'category': "Data Manipulation",
        'researchSubject': "Computer vision",
        'tags': "transition,detection,video,computer,vision",
        'home': "https://github.com/crim-ca/Service",
        'doc': "https://github.com/crim-ca/Service",
        'releasenotes': "https://github.com/crim-ca/Service",
        'support': "https://github.com/crim-ca/Service",


        # If the source are not provided, CANARIE requires a 204 (No content)
        # response
        'source': "https://github.com/crim-ca/Service",
        'tryme': "https://github.com/crim-ca/Service",
        'licence': "https://github.com/crim-ca/Service",
        'provenance': "https://github.com/crim-ca/Service",
        'os_args': {'image': 'transition_v_1.1.5',
                    'instance_type': 'm1.large'},
        # Process-request to spawn VM ratio
        'rubber_params': {'spawn_ratio': 0.1}
    },
    'faceanalysis': {
        'route_keyword': 'faceanalysis',
        'celery_task_name': 'faceanalysis',
        'celery_queue_name': 'faceanalysis',
        'name': 'Face detection service',
        'synopsis': "RESTful service providing face analysis in video.",
        'version': '1.0.1',  # Expected version - will check.
        'institution': 'CRIM',
        'releaseTime': '2015-01-01T00:00:00Z',
        'supportEmail': 'support-vesta@crim.ca',
        'category': "Data Manipulation",
        'researchSubject': "Computer vision",
        'tags': "face,detection,video,computer,vision",
        'home': "https://github.com/crim-ca/Service",
        'doc': "https://github.com/crim-ca/Service",
        'releasenotes': "https://github.com/crim-ca/Service",
        'support': "https://github.com/crim-ca/Service",


        # If the source are not provided, CANARIE requires a 204 (No content)
        # response
        'source': "https://github.com/crim-ca/Service",
        'tryme': "https://github.com/crim-ca/Service",
        'licence': "https://github.com/crim-ca/Service",
        'provenance': "https://github.com/crim-ca/Service",
        'os_args': {'image': 'transition_v_1.1.5',
                    'instance_type': 'm1.large'},
        # Process-request to spawn VM ratio
        'rubber_params': {'spawn_ratio': 0.1}
    },
}
