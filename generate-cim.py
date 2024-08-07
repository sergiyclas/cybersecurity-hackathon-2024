import xml.etree.ElementTree as ET


def generate_random_cim_model():
    root = ET.Element('Network')
    main_substation = ET.SubElement(root, 'Substation', id='substationMain')
    name = ET.SubElement(main_substation, 'Name')
    name.text = 'Головна підстанція'
    substation_count = 0
    transformer_count = 0
    ses_count = 0
    wes_count = 0
    consumer_count = 0

    for i in range(3):
        substation_count += 1
        substation_id = f"substation_{substation_count}"
        substation = ET.SubElement(root, "Substations", id=substation_id)
        name = ET.SubElement(substation, 'Name')
        name.text = f'Підстанція {substation_count}'
        connections = ET.SubElement(substation, 'Connections')
        connection = ET.SubElement(connections, 'Connection', to='substationMain')

        for j in range(2):
            transformer_count += 1
            transformer_id = f'transformer_{transformer_count}'
            transformer = ET.SubElement(substation, 'Transformer', id=transformer_id)
            name = ET.SubElement(transformer, 'Name')
            name.text = f'Трансформатор {transformer_count}'
            transformers_connections = ET.SubElement(transformer, 'Connections')
            transformers_connection = ET.SubElement(transformers_connections, 'Connection', to=substation_id)

            for k in range(2):
                wes_count += 1
                wes = ET.SubElement(transformer, 'Wes', id=f'wes_{wes_count}')
                name = ET.SubElement(wes, 'Name')
                name.text = f'Wes {wes_count}'
                wes_connections = ET.SubElement(wes, 'Connections')
                wes_connection = ET.SubElement(wes_connections, 'Connection', to=transformer_id)

            for k in range(2):
                ses_count += 1
                ses = ET.SubElement(transformer, 'Ses', id=f'ses_{ses_count}')
                name = ET.SubElement(ses, 'Name')
                name.text = f'Ses {ses_count}'
                ses_connections = ET.SubElement(ses, 'Connections')
                ses_connection = ET.SubElement(ses_connections, 'Connection', to=transformer_id)

            for k in range(5):
                consumer_count += 1
                consumer = ET.SubElement(transformer, 'Consumer', id=f'consumer_{consumer_count}')
                name = ET.SubElement(consumer, 'Name')
                name.text = f'Споживач {consumer_count}'
                consumers_connections = ET.SubElement(consumer, 'Connections')
                consumers_connection = ET.SubElement(consumers_connections, 'Connection', to=transformer_id)

        for j in range(1):
            substation_count += 1
            substation_sub_id = f"substation_{substation_count}"
            substation_sub = ET.SubElement(root, "Substations", id=substation_sub_id)
            name = ET.SubElement(substation_sub, 'Name')
            name.text = f'Підстанція {substation_count}'
            connections = ET.SubElement(substation_sub, 'Connections')
            connection = ET.SubElement(connections, 'Connection', to=substation_id)

            for k in range(1):
                transformer_count += 1
                transformer_id = f'transformer_{transformer_count}'
                transformer = ET.SubElement(substation_sub, 'Transformer', id=transformer_id)
                name = ET.SubElement(transformer, 'Name')
                name.text = f'Трансформатор {transformer_count}'
                transformers_connections = ET.SubElement(transformer, 'Connections')
                transformers_connection = ET.SubElement(transformers_connections, 'Connection', to=substation_sub_id)

                for g in range(2):
                    ses_count += 1
                    ses = ET.SubElement(transformer, 'Ses', id=f'ses_{ses_count}')
                    name = ET.SubElement(ses, 'Name')
                    name.text = f'Ses {ses_count}'
                    ses_connections = ET.SubElement(ses, 'Connections')
                    ses_connection = ET.SubElement(ses_connections, 'Connection', to=transformer_id)

                for g in range(7):
                    consumer_count += 1
                    consumer = ET.SubElement(transformer, 'Consumer', id=f'consumer_{consumer_count}')
                    name = ET.SubElement(consumer, 'Name')
                    name.text = f'Споживач {consumer_count}'
                    consumers_connections = ET.SubElement(consumer, 'Connections')
                    consumers_connection = ET.SubElement(consumers_connections, 'Connection', to=transformer_id)
    return root


def save_cim_model_to_xml(cim_model, output_file):
    tree = ET.ElementTree(cim_model)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)


if __name__ == '__main__':
    cim_model = generate_random_cim_model()
    output_file = f'data/cim_model.xml'
    save_cim_model_to_xml(cim_model, output_file)
    print(f'CIM model saved to {output_file}')