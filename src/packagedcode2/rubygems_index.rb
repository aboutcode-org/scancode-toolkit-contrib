#!/usr/bin/ruby
 
# Dump to stdout a JSON representation of the marshal-formatted Rubygems index.
# see https://blog.engineyard.com/2014/new-rubygems-index-format
# The output file is in the form: name, version, platform
# [
#   ["capistrano-rsync-scm","0.0.3","ruby"],
#   ["drpentode-scrivener","0.0.3","ruby"]
# ]

require 'rubygems/package'
require 'json'
 
 
def gemindex(rubygems_index_file)
  idx = Marshal.load(Gem.gunzip(File.read(rubygems_index_file)))
  puts JSON.pretty_generate(idx)
end
 
if __FILE__ == $PROGRAM_NAME
  rubygems_index_file = ARGV[0]
  gemindex(rubygems_index_file)
end
