try:
    from src.network import encoder, decoder
except:
    from diffworld.shape_as_points.src.network import encoder, decoder
encoder_dict = {
    'local_pool_pointnet': encoder.LocalPoolPointnet,
}
decoder_dict = {
    'simple_local': decoder.LocalDecoder,
}