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
      _format="{{self._private_keys_}}{{self._public_keys_}}"


// Some useful defaults for _i_width
@var IMG_SIZE="{{self._public_keys_}}"\
      thumb="{{var.IMG_DEF._null_(_i_width=\"20%\")}}"\
      small="{{var.IMG_DEF._null_(_i_width=\"40%\")}}"\
      medium="{{var.IMG_DEF._null_(._i_width=\"70%\")}}"\
      large="{{var.IMG_DEF._null_(_i_width=\"90%\")}}"\
      custom="{{var.IMG_DEF._null_(_i_width=\"{{self.w}}\")}}"\
      w="50%"

// Some useful shortcuts to select styling for an image
@var IMG_STYLE="{{self._public_keys_}}"\
      inline="{{var.IMG_DEF.img_st_inline}}"\
      inline_border="{{var.IMG_DEF.img_st_inline_border}}"\
      block="{{var.IMG_DEF.img_st_block}}"\
      block_border="{{var.IMG_DEF.img_st_block_border}}"
