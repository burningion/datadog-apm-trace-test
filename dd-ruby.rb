require 'ddtrace'

Datadog.configure do |c|
  # add hostname if running in a container
  # hostname: 'agent',
  c.tracer priority_sampling: true
end

Datadog.tracer.trace('web.request', service: 'ruby-trace-length-test') do |span|
  span.context.sampling_priority = Datadog::Ext::Priority::USER_KEEP
  sleep(ARGV[0].to_i)
  puts 'Slept ' + ARGV[0] + ' seconds.'

end

sleep(10)
