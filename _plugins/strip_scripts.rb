module StripScripts
  def strip_scripts(html)
    html.to_s.gsub(%r{<script\b.*?</script>}m, "")
  end
end

Liquid::Template.register_filter(StripScripts)
