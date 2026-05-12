module.exports = function(eleventyConfig) {
  // Copy these files/folders straight to the output without processing
  eleventyConfig.addPassthroughCopy("assets");

eleventyConfig.addFilter("dateDisplay", (dateObj) => {
    if (!dateObj) return "";
    return new Date(dateObj).toLocaleDateString("en-NZ", {
      year: "numeric", month: "long", day: "numeric"
    });
  });

  eleventyConfig.addFilter("dateISO", (dateObj) => {
    if (!dateObj) return "";
    return new Date(dateObj).toISOString().split("T")[0];
  });

  eleventyConfig.addFilter("readingTime", (content) => {
    if (!content) return "";
    const text = content.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
    const words = text.split(" ").filter(w => w.length > 0).length;
    const minutes = Math.ceil(words / 200);
    if (minutes <= 1) return "1 min";
    if (minutes >= 20) return "deep dive";
    return `${minutes} min`;
  });

  const TAG_LABELS = {
    redflags:    "Red flags",
    guidelines:  "Guidelines",
    hacks:       "Practical hacks",
    controversy: "Controversy",
    medicolegal: "Medico-legal",
    patient:     "Patient comms"
  };
  eleventyConfig.addFilter("tagLabel", (tag) => TAG_LABELS[tag] || tag);

  // Site-wide config
  return {
    dir: {
      input: ".",
      output: "_site",
      includes: "_includes",
      layouts: "_layouts",
      data: "_data"
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    templateFormats: ["md", "njk", "html"]
  };
};