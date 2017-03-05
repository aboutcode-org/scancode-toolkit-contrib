#!/usr/bin/ruby
# -*- encoding: utf-8 -*-

# Dump a gemspec as JSON to stdout from a .gem file or a .gemspec file

require 'rubygems/package'
require 'json'

begin
  # only available in older rubygems 1.8.x 
  require 'rubygems/format'
  rescue LoadError
end


def gemspec(gem_or_spec)
  if gem_or_spec.end_with?('.gem')
    # try rubygems 2.x syntax then fallback to 1.8
    gem_spec = gem_spec = Gem::Package.new(gem_or_spec).spec rescue Gem::Format.from_file_by_path(gem_or_spec).spec 

  elsif gem_or_spec.end_with?('.gemspec')
    gem_spec = Gem::Specification.load(gem_or_spec)
  end

  spec_vars = {}
  gem_spec.instance_variables.each { |var| spec_vars[var.to_s.delete("@")] = gem_spec.instance_variable_get(var) }
  puts JSON.pretty_generate(spec_vars)
end

 
if __FILE__ == $PROGRAM_NAME
  gem_file = ARGV[0]
  gemspec(gem_file)
end
