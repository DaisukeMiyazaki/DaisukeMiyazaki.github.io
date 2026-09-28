# トップの流れやフィードで本文を加工する Liquid フィルター
module StreamFilters
  VOID_ELEMENTS = %w[area base br col embed hr img input link meta source track wbr].freeze
  TAG = %r{<(/?)([a-zA-Z][\w-]*)\b[^>]*?(/?)>}

  def strip_scripts(html)
    html.to_s.gsub(%r{<script\b.*?</script>}m, "")
  end

  # loading 属性のない img を遅延読み込みにする
  def lazy_images(html)
    html.to_s.gsub(/<img\b(?![^>]*\bloading=)/i, '<img loading="lazy" decoding="async"')
  end

  # 先頭から n 個のトップレベル要素だけを残す
  def first_blocks(html, n)
    html = strip_comments(html)
    ends = block_ends(html)
    ends.size > n ? html[0...ends[n - 1]] : html
  end

  def block_count(html)
    block_ends(strip_comments(html)).size
  end

  private

  def strip_comments(html)
    html.to_s.gsub(/<!--.*?-->/m, "")
  end

  # トップレベル要素それぞれの終わりの位置
  def block_ends(html)
    depth = 0
    ends = []
    html.scan(TAG) do
      m = Regexp.last_match
      if m[1] == "/"
        depth -= 1
      elsif !(VOID_ELEMENTS.include?(m[2].downcase) || m[3] == "/")
        depth += 1
        next
      end
      ends << m.end(0) if depth.zero?
    end
    ends
  end
end

Liquid::Template.register_filter(StreamFilters)
