/**
 * Add book data from JSON strings to a slides presentation
 */

var slide;
var json;
var jsonString = '';
var slideWidth = 720;
var slideHeight = (9/16) * slideWidth;

/**
 * Run the tasks
 */
function myFunction() {
  // Array of all the JSON strings for each book
  var jsonStrings = [
    // JSON strings go inside this array
  ];
  for(var i = 0; i < jsonStrings.length; i++) {
    presentData(jsonStrings[i]);
  }
}

/**
 * Retrieve and display the a book's data on the slide
 * @param {string} jsonString - string containing the JSON data from the Python script 
 */
function presentData(jsonString) {
  var presentation = SlidesApp.getActivePresentation();
  slide = presentation.appendSlide();

  // Add background image;
  // Easiest way I could figure out to host an image was through GitHub
  addImage("https://raw.githubusercontent.com/zachm01/Book-Information/main/bookdata/data/ppt_bg.png", 0, 0, slideWidth, slideHeight);

  var id = slide.insertTextBox("z");
  id.setTop(-7);
  id.setLeft(700);

  // Add information
  json = JSON.parse(jsonString);
  var keys = [];
  for(var key in json) { keys.push(key); }

  let title = json["title"] + " by " + json["author"];

  // Title and synopsis
  addText(title, "Libre Baskerville", 20, 1000, 21, 25);
  addText(json["synopsis"], "Libre Baskerville", 12, 290, 60, 25);

  // Side text

  var identifiers = ["Genre", "Avg. Rating", "[place in series]", "[age suggestion]", "Published", "PC"];
  var keys = ["genres", "rating", "", "", "published in", "page count"];

  for(let i = 0; i < identifiers.length; i++) {
    addSideText(identifiers[i], keys[i], i);

  }
  
  // Cover image
  addImage(json["cover"], 67, 480, 200, 300);
}

/**
 * Add text to the slide presentation
 * @param {string} title - text information of the text object
 * @param {string} font - font family of the text
 * @param {int} fontSize - size of the text
 * @param {int} width - width of the text box
 * @param {int} top - distance from the top of the slide to the top of the text box
 * @param {int} left - distance from the very left of the slide to the left of the text box
 */
function addText(title, font, fontSize, width, top, left) {
  var t = slide.insertTextBox(title)
  var tRange = t.getText();
  var tStyle = tRange.getTextStyle();
  tStyle.setFontFamily(font)
  tStyle.setFontSize(fontSize);
  tStyle.setForegroundColor("#80694c");
  t.setWidth(width);
  t.setTop(top);
  t.setLeft(left);
}

/**
 * Add the side information text in between the cover image and the synopsis text
 * @param {string} identifier - name of the property
 * @param {string} key - name of the property in the JSON string
 * @param {int} pos - relative position of the side info text, i.e. 0, 1, 2, 3...
 */
function addSideText(identifier, key, pos) {
  var temp;
  // If the key returns an array, choose first element of array
  if(typeof(json[key]) == "object") {
    temp = json[key][0];
  } else {
    temp = json[key];
  }
  addText(`${identifier}: ${temp}`, "Roboto", 14, 150, 80 + pos*50, 320);
}

/**
 * Add an image to the presentation from a URL
 * @param {string} url_ - URL of the image
 * @param {int} top - distance from the top of the slide to the top of the image
 * @param {int} left - distacne from the left of the slide to the left of the image
 * @param {int} w - width of the image
 * @param {int} h - height of the image
 */
function addImage(url_, top, left, w, h) {
  // Adds an image from a url
  // For book covers, left ≈ 450, top ≈ 50
  const url = url_;
  var image = slide.insertImage(url);
  image.setTop(top);
  image.setLeft(left);
  image.setWidth(w);
  image.setHeight(h);
}


