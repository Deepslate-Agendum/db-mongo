from db_python_util.db_classes import TaskType, Field, ValueType, AllowedValue
from db_python_util.db_helper import ConnectionManager


# function that creates the default task type and saves it to the database
@ConnectionManager.requires_connection
def createDefaultTaskType():

    # create a Tag Value Type
    tag_value_type = ValueType(
        name="Tag",
        allowed_values=[]
    )
    tag_value_type.save()

    # create a Manner Value Type
    manner_value_type = ValueType(
        name="Manner",
        allowed_values=[]
    )
    manner_value_type.save()

    # create Blocking and Subtask Fields using Manner Value Type
    blocking_manner = AllowedValue(
        value="Blocking",
        value_type=manner_value_type,
    )
    blocking_manner.save()

    subtask_manner = AllowedValue(
        value="Subtask",
        value_type=manner_value_type,
    )
    subtask_manner.save()

    manner_value_type.allowed_values = [blocking_manner, subtask_manner]
    manner_value_type.save()


    # create default ValueTypes: string and user
    string_value_type = ValueType(
        name="String",
        allowed_values=[]
    )
    user_value_type = ValueType(
        name="User",
        allowed_values=[]
    )
    string_value_type.save()
    user_value_type.save()

    # create system fields: Name, Assignee, Description, Due Date
    name_system_field = Field(
        name="Name",
        min_values=1,
        max_values=1,
        default_allowed_value=None,
        value_type=string_value_type,
    )
    assignee_system_field = Field(
        name="Assignee",
        min_values=0,
        max_values=1,
        default_allowed_value=None,
        value_type=user_value_type,
    )
    description_system_field = Field(
        name="Description",
        min_values=1,
        max_values=1,
        default_allowed_value=None,
        value_type=string_value_type,
    )
    due_date_system_field = Field(
        name="Due Date",
        min_values=0,
        max_values=1,
        default_allowed_value=None,
        value_type=string_value_type,
    )
    name_system_field.save()
    assignee_system_field.save()
    description_system_field.save()
    due_date_system_field.save()

    # create default task type
    default_task_type = TaskType(
        name="Default",
        static_fields=[],
        nonstatic_fields=[
            name_system_field,
            assignee_system_field,
            description_system_field,
            due_date_system_field,
        ],
        static_field_values=[],
        workspaces=[],
        dependency_groups=[],
    )
    default_task_type.save()


def main():
    createDefaultTaskType()


if __name__ == "__main__":
    main()
