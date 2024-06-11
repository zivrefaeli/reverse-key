require 'fluent/plugin/filter'

module Fluent::Plugin
  class ReverseKey < Filter
    Fluent::Plugin.register_filter('reverse_key', self)

    desc 'The key to reverse'
    config_param :key, :string, default: 'message'

    def filter(tag, time, record)
      begin
        record[@key] = record[@key].reverse
      rescue
        log.error('failed to reverse %s at %s' % [@key, record])
        return nil
      else
        return record
      end
    end
  end
end
