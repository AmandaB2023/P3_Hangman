from colorama import Fore, Style
hangman_visual_dict = {
        0: f"""{Fore.RED}
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |

               H A N G M A N !!
           """,
        1: f"""{Fore.GREEN}
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |

                H A N G M A _
            """,
        2: f"""{Fore.GREEN}
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |

               H A N G M _ _
            """,
        3: f"""{Fore.GREEN}
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |

               H A N G _ _ _
            """,
        4: f"""{Fore.GREEN}
                ___________
               | /        | 
               |/        
               |          
               |          
               |

               H A N _ _ _ _
            """,
        5: f"""{Fore.GREEN}
                ___________
               | /        
               |/        
               |          
               |          
               |

               H A _ _ _ _ _
            """,
        6: f"""{Fore.GREEN}
               |
               |
               |
               |
               |

               H _ _ _ _ _ _
               
        ******************************* 
            """,
        7:f"""{Fore.GREEN}
                _ _ _ _ _ _ _

        *******************************  {Style.RESET_ALL}     
          """,
    }