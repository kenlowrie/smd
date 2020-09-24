// Create a constant var with various styles and defaults for images

@var _id="IMG_DEF" \
      _i_width="90%" \
      _b_size="1px" \
      _b_type="solid" \
      img_border_style="border:{{self._b_size}} {{self._b_type}};padding:1em;" \
      img_inline_style="margin-left:auto;margin-right:auto;width:{{self._i_width}};" \
      img_st_inline="{{self.img_inline_style}}" \
      img_st_inline_border="{{self.img_inline_style}}{{self.img_border_style}}" \
      img_st_block="display:block;{{self.img_inline_style}}" \
      img_st_block_border="display:block;{{self.img_inline_style}}{{self.img_border_style}}" \
      _format="{{self._private_keys_}}{{self._public_keys_}}"\
      _help="[sp.2]*{{self._}}*[bb]\
[sp.4]Defines common image styling options.[bb][sp.4]Not normally accessed directly. Used by **IMG_SIZE** and **IMG_STYLE** as helpers.[bb]\
[sp.2]**Common Attribute Values**[b]\
[sp.4]**_i_width** - width: CSS value[b]\
[sp.4]**_b_size** - border: CSS size value[b]\
[sp.4]**_b_type** - border: CSS type value[bb]\
[sp.2]**Common Styling Defaults**[b]\
[sp.4]**img_border_style** - CSS styling for bordered image[b]\
[sp.4]**img_inline_style** - CSS styling for borderless image[bb]\
[sp.2]**Common Image Style Options**[b]\
[sp.4]**img_st_inline** - CSS styling for inline image[b]\
[sp.4]**img_st_inline_border** - CSS styling for inline bordered image[b]\
[sp.4]**img_st_block** - CSS styling for block image[b]\
[sp.4]**img_st_block_border** - CSS styling for block bordered image."

// Some useful defaults for _i_width
@var IMG_SIZE="{{self._public_keys_}}"\
      thumb="{{var.IMG_DEF._null_(_i_width=\"20%\")}}"\
      small="{{var.IMG_DEF._null_(_i_width=\"40%\")}}"\
      medium="{{var.IMG_DEF._null_(._i_width=\"70%\")}}"\
      large="{{var.IMG_DEF._null_(_i_width=\"90%\")}}"\
      custom="{{var.IMG_DEF._null_(_i_width=\"{{self.w}}\")}}"\
      w="50%"\
      _help="[sp.2]*{{self._}}*[bb]\
[sp.4]Provides methods for common image sizes.[bb][sp.4]Use them when you want to change the default image size used in the **IMG_STYLE** attributes.[bb]\
[sp.2]**Common Methods**[b]\
[sp.4]**thumb** - Sets **IMG_DEF._i_width** to 20%[b]\
[sp.4]**small** - Sets **IMG_DEF._i_width** to 40%[b]\
[sp.4]**medium** - Sets **IMG_DEF._i_width** to 70%[b]\
[sp.4]**large** - Sets **IMG_DEF._i_width** to 90%[b]\
[sp.4]**custom(w)** - Sets **IMG_DEF._i_width** to **w**[bb]\
[sp.2]**Examples**[b]\
[sp.4]**[E.lb]IMG_SIZE.small[E.rb]** - Sets **IMG_DEF._i_width** to **20%**[b]\
[sp.4]**[E.lb]IMG_SIZE.custom[E.lp]w=\"50%\"[E.rp][E.rb]** - Sets **IMG_DEF._i_width** to **50%**."

// Some useful shortcuts to select styling for an image
@var IMG_STYLE="{{self._public_keys_}}"\
      inline="{{var.IMG_DEF.img_st_inline}}"\
      inline_border="{{var.IMG_DEF.img_st_inline_border}}"\
      block="{{var.IMG_DEF.img_st_block}}"\
      block_border="{{var.IMG_DEF.img_st_block_border}}"\
      _help="[sp.2]*{{self._}}*[bb]\
[sp.4]Several styling attributes for common image styles.[bb][sp.4]These attributes are used to obtain various CSS styles for an @image variable.[bb]\
[sp.2]**Common Attributes**[b]\
[sp.4]**inline** - Returns **IMG_DEF.img_st_inline**[b]\
[sp.4]**inline_border** - Returns **IMG_DEF.img_st_inline_border**[b]\
[sp.4]**block** - Returns **IMG_DEF.img_st_block**[b]\
[sp.4]**block_border** - Returns **IMG_DEF.img_st_block_border**[b]\
[sp.2]**Examples**[b]\
[sp.4]**[E.lb]IMG_STYLE.inline[E.rb]** - Returns the CSS to style an inline image[b]\
[sp.4]**[E.lb]IMG_STYLE.block_border[E.rb]** - Returns the CSS to style a block image with a border."
