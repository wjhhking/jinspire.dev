require 'sinatra'
require 'json'
require 'date'

post '/log' do
  data = JSON.parse(request.body.read)
  File.open('visits.log', 'a') do |f|
    f.puts "#{Time.now.iso8601},#{data['page']},#{request.ip}"
  end
  status 204
end 