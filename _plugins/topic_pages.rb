module TopicPages
  class TopicPage < Jekyll::PageWithoutAFile
    def initialize(site, lang, topic, posts)
      super(site, site.source, File.join(lang, "topics", topic), "index.html")
      data["layout"] = "topic"
      data["lang"] = lang
      data["topic"] = topic
      data["title"] = topic
      data["posts"] = posts
    end
  end

  class Generator < Jekyll::Generator
    safe true

    def generate(site)
      site.data["topics_by_lang"] = {}

      site.posts.docs.group_by { |doc| doc.data["lang"] }.each do |lang, docs|
        next if lang.nil?

        keys = docs.flat_map { |doc| Array(doc.data["topics"]) }.uniq.sort
        site.data["topics_by_lang"][lang] = keys

        keys.each do |topic|
          posts = docs.select { |doc| Array(doc.data["topics"]).include?(topic) }
                      .sort_by(&:date).reverse
          site.pages << TopicPage.new(site, lang, topic, posts)
        end
      end
    end
  end
end
