module TopicPages
  class TopicPage < Jekyll::PageWithoutAFile
    def initialize(site, lang, topic, entries)
      super(site, site.source, File.join(lang, "topics", topic), "index.html")
      data["layout"] = "topic"
      data["lang"] = lang
      data["topic"] = topic
      data["title"] = topic
      data["entries"] = entries
    end
  end

  class Generator < Jekyll::Generator
    safe true

    def generate(site)
      site.data["topics_by_lang"] = {}

      docs = site.posts.docs + site.collections["notes"].docs
      docs.group_by { |doc| doc.data["lang"] }.each do |lang, lang_docs|
        next if lang.nil?

        keys = lang_docs.flat_map { |doc| Array(doc.data["topics"]) }.uniq.sort
        site.data["topics_by_lang"][lang] = keys

        keys.each do |topic|
          entries = lang_docs.select { |doc| Array(doc.data["topics"]).include?(topic) }
                             .sort_by(&:date).reverse
          site.pages << TopicPage.new(site, lang, topic, entries)
        end
      end
    end
  end
end
