task :p1 do 
  sh "python 1.py | sh | tippecanoe-json-tool > 1.geojsons"
end

task :p2 do
  sh <<-EOS
python 2.py | tippecanoe -o 14321.pmtiles --force \
--maximum-zoom=16 --minimum-zoom=4
  EOS
end
