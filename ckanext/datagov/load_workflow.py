import os
import json
import logging
from ckan.plugins import toolkit
from ckan import model

# Create a logger for this module
logger = logging.getLogger(__name__)

def load_workflow_configuration():
    # Load the workflow configuration path from environment variable
    config_path = os.getenv('CKAN__WORKFLOW__JSON_CONFIG')

    if config_path and os.path.isfile(config_path):
        try:
            with open(config_path) as json_file:
                workflow_config = json.load(json_file)

                # Register the workflow states in CKAN
                for workflow_name, workflow_data in workflow_config.get('workflows', {}).items():
                    toolkit.get_action('workflow_create')(data_dict={
                        'name': workflow_name,
                        'label': workflow_data['label'],
                        'states': workflow_data['states'],
                        'start_state': workflow_data['start_state'],
                    })
                
                logger.info("Successfully loaded workflow configuration from: %s", config_path)

        except Exception as e:
            logger.error("Failed to load workflow configuration: %s", e)

    else:
        logger.error("Workflow configuration file not found or invalid path: %s", config_path)
# Hook into the package create action
def dataset_created(context, data_dict):
    package = model.Package.get(data_dict['id'])
    toolkit.get_action('workflow_init')(data_dict={'id': package.id})

toolkit.get_action('package_create').after_update = dataset_created

# Hook into the organization create action
def organization_created(context, data_dict):
    org = model.Group.get(data_dict['id'])
    toolkit.get_action('workflow_init')(data_dict={'id': org.id})

toolkit.get_action('organization_create').after_update = organization_created

# Call the configuration load on extension initialization
load_workflow_configuration()
