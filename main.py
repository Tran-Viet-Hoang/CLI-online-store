# FINAL Introduction to Programming assignment

# This project features an online store running on CLI. This online store sells books.

# an item should have the following attributes:
# {id, price, total_quantity, colors(quantity of each), weight, size, tech specs, reviews}

master_dictionary = {
    "Iphone 13 Pro Max": {
        "id": "1001",
        "price": 32000000,
        "total_quantity": 40,
        "colors": {
            "blue": 10,
            "green": 10,
            "purple": 10,
            "white": 10},
        "weight": "240 grams",
        "sizes": "6.7 inches",
        "tech specs": """
            IP68 Water Resistance,
            A15 Bionic chip
            New 6‑core CPU with 2 performance and 4 efficiency cores
            New 5‑core GPU
            New 16‑core Neural Engine
            Pro 12MP camera system: Telephoto, Wide, and Ultra Wide cameras
            Cinematic mode for recording videos with shallow depth of field (1080p at 30 fps)
            FaceID 
            22 hours of video playback with a single charge
            For more info, checkout the product's official website:https://www.apple.com/vn/iphone-13-pro/specs""",
        "reviews": {"likes": 0, "dislikes": 0}
    },
    "Iphone 13 Pro": {
        "id": "1002",
        "price": 32000000,
        "total_quantity": 40,
        "colors": {
            "blue": 10,
            "green": 10,
            "purple": 10,
            "white": 10},
        "weight": "200 grams",
        "sizes": "6.1 inches",
        "tech specs": """
            IP68 Water Resistance,
            A15 Bionic chip
            New 6‑core CPU with 2 performance and 4 efficiency cores
            New 5‑core GPU
            New 16‑core Neural Engine
            Pro 12MP camera system: Telephoto, Wide, and Ultra Wide cameras
            Cinematic mode for recording videos with shallow depth of field (1080p at 30 fps)
            FaceID
            22 hours of video playback with a single charge
            For more info, checkout the product's official website:https://www.apple.com/vn/iphone-13-pro/specs""",
        "reviews": {"likes": 0, "dislikes": 0}
    },
    "Nvidia RTX 3090": {
        "id": "1003",
        "price": 69999000,
        "total_quantity": 10,
        "weight": "2100 grams",
        "sizes": "12.1 inches",
        "tech specs": """
           NVIDIA CUDA Cores 10496	
           Boost Clock 1.70 GHZ
           Memory Size 24 GB
           Memory Type GDDR6X
           For more info, checkout the product's official website:https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090/""",
        "reviews": {"likes": 0, "dislikes": 0}
    },
    "Nike Dior Jordan 1": {
        "id": "1004",
        "price": 534028000,
        "total_quantity": 2,
        "colors": {
            "white": 2},
        "weight": "420 grams",
        "sizes": "11",
        "specs": """
            Release July 2020
            Only 8500 pairs were made
            Release price was $2200
            Could be up to $20k
            For more info, checkout the product's official website:https://www.highsnobiety.com/p/dior-nike-air-jordan-1/#:~:text=Air%20Jordan%201%20Dior%20release,ups%20and%20pop-in%20stores.""",
        "reviews": {"likes": 0, "dislikes": 0}
    },

}
shopping_cart = {"items": [], "total_price": 0}

while True:
    display_list = []
    new_list = []


    def get_all_items():
        for j, k in master_dictionary.items():
            if j not in new_list:
                new_list.append(j)
            print(j)
        return new_list


    def get_items_details():
        for j, k in master_dictionary.items():
            print(j, k)


    def filter_by_name(search_input):
        for e in new_list:
            if search_input in e.replace(" ", "").lower():
                display_list.append(e)


    def filter_by_id(search_input):
        for e in new_list:
            if search_input in e["id"]:
                display_list.append(e)


    user_input = int(input("input a name: ").lower().replace(" ", ""))
    if user_input == "/stop":
        break
    else:
        get_all_items()
        print(new_list)
        # filter_by_name(user_input)
        filter_by_id(user_input)
        print(display_list)
