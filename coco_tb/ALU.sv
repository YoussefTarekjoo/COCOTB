module ALU (
    input wire clk , reset ,
    input wire [1:0] Opcode ,	// The opcode
    input wire  signed [3:0] A ,	// Input data A in 2's complement
    input wire signed [3:0] B ,	// Input data B in 2's complement
    output reg signed [7:0] C , // ALU output in 2's complement
		  );
		  
	// Define constants
    localparam MAXPOS = 7 ;
    localparam MAXNEG = -8 ;
    localparam ZERO   = 0 ;

    parameter ADD                 = 2'b00 ; 
    parameter SUB                 = 2'b01 ;
    parameter MULT                = 2'b10 ;
    parameter DIV                 = 2'b11 ;
		  
	reg signed [7:0] Alu_out ;

   // Do the operation
   always @* begin
      case (Opcode)
      	ADD:            Alu_out = A + B;
      	SUB:            Alu_out = A - B;
      	MULT:           Alu_out = A * B;
      	DIV: begin
		  if(B == 0)
		   begin
			Alu_out = 8'hff;
		   end
		  else
		   begin
		    Alu_out = A / B;
		   end
		end
        default:        Alu_out = 8'b0 ;
      endcase
   end 
   
   always @(posedge clk or negedge reset) begin
      if (!reset)
	   begin
	     C <= 8'b0;
	   end
      else
	   begin
	     C <= Alu_out;
	   end
   end

endmodule
