import xml.etree.ElementTree as ET


def parse_sim(path):
    tree = ET.parse(path)
    root = tree.getroot()

    transformer_to_substation = {}
    consumer_to_transformer = {}
    generator_to_transformer = {}

    def extract_id_from_ref(ref):
        return ref.split('#')[-1] if ref else None

    for transformer in root.findall('.//Transformer'):
        transformer_id = transformer.get('id')
        connections = transformer.find('Connections')
        if connections:
            for connection in connections.findall('Connection'):
                to_id = connection.get('to')
                if to_id and to_id.startswith('substation_'):
                    transformer_to_substation[transformer_id] = to_id

    for consumer in root.findall('.//Consumer'):
        consumer_id = consumer.get("id")
        connections = consumer.find("Connections")
        if connections:
            for connection in connections.findall("Connection"):
                to_id = connection.get('to')
                if to_id and to_id.startswith('transformer_'):
                    consumer_to_transformer[consumer_id] = to_id

    for generator in root.findall('.//Generator'):
        generator_id = generator.get("id")
        connections = generator.find("Connections")
        if connections:
            for connection in connections.findall("Connection"):
                to_id = connection.get('to')
                if to_id and to_id.startswith('transformer_'):
                    generator_to_transformer[generator_id] = to_id
    return transformer_to_substation, consumer_to_transformer, generator_to_transformer


if __name__ == '__main__':
    # d1, d2, d3 = parse_sim("cim_model.xml")
    pass
