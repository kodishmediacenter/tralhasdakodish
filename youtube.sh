ids = input('Digite o ID youtube: ')

new_path = 'video.html'
new_vod = open(new_path,'w')
new_vod.write('<iframe width="560" height="315" src="https://www.youtube.com/embed/'+ids+'" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
