from pygal_maps_world.maps import World
wm = World()
wm.force_uri_protocol = 'http'
wm.title = 'North America'
wm.add('North America', ['ca', 'mx', 'us'])
wm.render_to_file('north_america.svg') 
