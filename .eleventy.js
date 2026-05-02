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