def localize_objects(path):

    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    objects = client.object_localization(image=image).localized_object_annotations

    object_list = ""

    for object in objects:
        object_list = object_list + "#" + object.name.lower() + " "

    print(object_list)

#    print('Number of objects found: {}'.format(len(objects)))
#    for object_ in objects:
#        print('\n{} (confidence: {})'.format(object_.name, object_.score))
#        print('Normalized bounding polygon vertices: ')
#        for vertex in object_.bounding_poly.normalized_vertices:
#            print(' - ({}, {})'.format(vertex.x, vertex.y))

localize_objects("images/brussels-public-domain.jpg")