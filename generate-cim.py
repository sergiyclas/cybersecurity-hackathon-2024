import xml.etree.ElementTree as ET
import random

def generate_random_cim_model():
    root = ET.Element('Network')
    main_substation = ET.SubElement(root, 'Substation', id='substationMain')
    name = ET.SubElement(main_substation, 'Name')
    name.text = 'Головна підстанція'

    for i in range(random.randint(2, 6)):
        substation_id = f"substation_{i}"
        substation = ET.SubElement(root, "Substations", id=substation_id)
        name = ET.SubElement(substation, 'Name')
        name.text = f'Підстанція {i}'
        connections = ET.SubElement(substation, 'Connections')
        connection = ET.SubElement(connections, 'Connection', to='substationMain')

        for j in range(random.randint(1, 4)):
            transformer_id = f'transformer_{i}_{j}'
            transformer = ET.SubElement(substation, 'Transformer', id=transformer_id)
            name = ET.SubElement(transformer, 'Name')
            name.text = f'Трансформатор {i}_{j}'
            transformers_connections = ET.SubElement(transformer, 'Connections')
            transformers_connection = ET.SubElement(transformers_connections, 'Connection', to=substation_id)

            for k in range(random.randint(0, 5)):
                generator = ET.SubElement(transformer, 'Generator', id=f'generator_{i}_{j}_{k}')
                name = ET.SubElement(generator, 'Name')
                name.text = f'Генератор {i}_{j}_{k}'
                generators_connections = ET.SubElement(generator, 'Connections')
                generators_connection = ET.SubElement(generators_connections, 'Connection', to=transformer_id)

            for k in range(random.randint(1, 10)):
                consumer = ET.SubElement(transformer, 'Consumer', id=f'consumer_{i}_{j}_{k}')
                name = ET.SubElement(consumer, 'Name')
                name.text = f'Споживач {i}_{j}_{k}'
                consumers_connections = ET.SubElement(consumer, 'Connections')
                consumers_connection = ET.SubElement(consumers_connections, 'Connection', to=transformer_id)
        
        for j in range(random.randint(0, 2)):
            substation_sub_id = f"substation_{i}_{j}"
            substation_sub = ET.SubElement(root, "Substations", id=substation_sub_id)
            name = ET.SubElement(substation_sub, 'Name')
            name.text = f'Підстанція {i}_{j}'
            connections = ET.SubElement(substation_sub, 'Connections')
            connection = ET.SubElement(connections, 'Connection', to=substation_id)

            for k in range(random.randint(1, 4)):
                transformer_id = f'transformer_{i}_{j}_{k}'
                transformer = ET.SubElement(substation_sub, 'Transformer', id=transformer_id)
                name = ET.SubElement(transformer, 'Name')
                name.text = f'Трансформатор {i}_{j}_{k}'
                transformers_connections = ET.SubElement(transformer, 'Connections')
                transformers_connection = ET.SubElement(transformers_connections, 'Connection', to=substation_sub_id)

                for g in range(random.randint(0, 5)):
                    generator = ET.SubElement(transformer, 'Generator', id=f'generator_{i}_{j}_{k}_{g}')
                    name = ET.SubElement(generator, 'Name')
                    name.text = f'Генератор {i}_{j}_{k}_{g}'
                    generators_connections = ET.SubElement(generator, 'Connections')
                    generators_connection = ET.SubElement(generators_connections, 'Connection', to=transformer_id)

                for k in range(random.randint(1, 10)):
                    consumer = ET.SubElement(transformer, 'Consumer', id=f'consumer_{i}_{j}_{k}_{g}')
                    name = ET.SubElement(consumer, 'Name')
                    name.text = f'Споживач {i}_{j}_{k}_{g}'
                    consumers_connections = ET.SubElement(consumer, 'Connections')
                    consumers_connection = ET.SubElement(consumers_connections, 'Connection', to=transformer_id)
    return root

def save_cim_model_to_xml(cim_model, output_file):
    tree = ET.ElementTree(cim_model)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

if __name__ == '__main__':
    cim_model = generate_random_cim_model()
    output_file = f'cim_model.xml'
    save_cim_model_to_xml(cim_model, output_file)
    print(f'CIM model saved to {output_file}')