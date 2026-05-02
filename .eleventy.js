module.exports = function(eleventyConfig) {
  // Copy these files/folders straight to the output without processing
  eleventyConfig.addPassthroughCopy("assets");

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