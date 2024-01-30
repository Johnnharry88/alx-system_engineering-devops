#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:9.*?)\] \[fags:(.*?\]/).join(",")
