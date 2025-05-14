from db_python_util.db_classes import TaskType, Field, ValueType, AllowedValue
from db_python_util.db_helper import ConnectionManager


def create_enum(enum_name, value_names):
    value_type = ValueType(
        name=enum_name,
        allowed_values=[],
    )
    value_type.save()

    values = []
    for value_name in value_names:
        value = AllowedValue(
            value=value_name,
            value_type=value_type,
        )
        value.save()
        values.append(value)

    value_type.update(allowed_values=values)
    value_type.save()

    return value_type, values

# function that creates the default task type and saves it to the database
@ConnectionManager.requires_connection
def createDefaultTaskType():
    tag_value_type, () = create_enum("Tag", [])


    manner_type, (blocking_manner, subtask_manner) = create_enum("Manner", ["Blocking", "Subtask"])

    status_type, (incomplete_status, in_progress_status, complete_status) = create_enum("Status", ["Incomplete", "In Progress", "Complete"])

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
    x_location_system_field = Field(
        name="X Location",
        min_values=0,
        max_values=1,
        default_allowed_value=None,
        value_type=string_value_type
    )
    y_location_system_field = Field(
        name="Y Location",
        min_values=0,
        max_values=1,
        default_allowed_value=None,
        value_type=string_value_type
    )
    tags_system_field = Field(
        name="Tags",
        min_values=0,
        value_type=tag_value_type,
    )

    name_system_field.save()
    assignee_system_field.save()
    description_system_field.save()
    due_date_system_field.save()
    x_location_system_field.save()
    y_location_system_field.save()
    tags_system_field.save()

    # create default task type
    default_task_type = TaskType(
        name="Default",
        static_fields=[],
        nonstatic_fields=[
            name_system_field,
            assignee_system_field,
            description_system_field,
            due_date_system_field,
            x_location_system_field,
            y_location_system_field,
            tags_system_field, # TODO: unlike other fields, static tags should be combined rather than overriden (but static fields in general are out of scope right now)
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
