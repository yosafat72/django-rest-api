def transform(values):
    arr = []

    for item in values:
        arr.append(singleTransform(item))
    return arr


def singleTransform(values):
    return {
        "id": values.id,
        "name": values.name,
        "dob": values.dob,
        "gender": values.gender,
        "phone": values.phone,
        "email": values.email,
        "address": values.address,
        "created_at": values.created_at,
        "updated_at": values.updated_at
    }
