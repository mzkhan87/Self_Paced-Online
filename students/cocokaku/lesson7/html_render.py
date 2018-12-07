class Element:
    tag = "html"
    indent = "   "

    def __init__(self, content=None):
        """
        initialize the Element instance
        
        :param content: optional input, string to create single line of content
        """
        self.content = []
        if content:
            self.content.append(content)

    def append(self, content):
        """
        append another line to content
        
        :param content: string to append
        :return: none
        """
        if content:
            self.content.append(content)

    def render(self, file_out, cur_ind=""):
        """
        render Element instance
        
        :param file_out: object to write rendering to
        :param cur_ind: indentation level to apply to each line
        :return: none
        """
        file_out.write(cur_ind+"<"+self.tag+">"+'\n')
        for item in self.content:
            if issubclass(type(item),Element):
                item.render(file_out, cur_ind+"   ")
            else:
                file_out.write(cur_ind+self.indent+item+'\n')
        file_out.write(cur_ind+"</"+self.tag+">"+'\n')


class Html(Element):
    tag = "html"


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def __init__(self, content=""):
        """
        initialize the OneLineTag instance
        
        :param content: 
        """
        self.content = content

    def append(self, content):
        """
        append if content is currently blank, otherwise do nothing (do not update or add)
        
        :param content: 
        :return: 
        """
        if not self.content:
            self.content = content

    def render(self, file_out, cur_ind=""):
        """
        render OneLineTag instance
        
        :param file_out: 
        :param cur_ind: 
        :return: 
        """
        file_out.write(cur_ind+"<"+self.tag+">"+self.content+"</"+self.tag+">"+'\n')



class Title(OneLineTag):
    tag = "title"
